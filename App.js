// Main React component for the Workout App (Front-End Only)
// This version expects all split/exercise data to come from the backend (Python)
// Only UI, user input, and check-in logic remain

function App() {
  // Add a new state for the selected goal
  const [goal, setGoal] = React.useState('');
  const [showGoalScreen, setShowGoalScreen] = React.useState(true);
  const [days, setDays] = React.useState(3);
  const [equipment, setEquipment] = React.useState(['None']);
  const [schedule, setSchedule] = React.useState([]);
  const [showSchedule, setShowSchedule] = React.useState(false);
  const [checkedIn, setCheckedIn] = React.useState([]);

  // All equipment options
  const ALL_EQUIPMENT = [
    'None',
    'Dumbbell',
    'Resistance Bands',
    'Barbells',
    'Kettlebells',
    'Full Gym'
  ];

  // Handle equipment selection (UI only)
  function handleEquipmentChange(e) {
    const value = e.target.value;
    setEquipment(prev =>
      prev.includes(value)
        ? prev.filter(eq => eq !== value)
        : [...prev.filter(eq => eq !== 'None'), value]
    );
  }

  // Handle goal selection
  function handleGoalSelect(selectedGoal) {
    setGoal(selectedGoal);
    setShowGoalScreen(false);
  }

  // On submit, fetch split/exercise data from backend (placeholder for now)
  function handleSubmit(e) {
    e.preventDefault();
    // TODO: Replace this with a fetch call to your Python backend
    // Example:
    // fetch(`/api/generate?days=${days}&equipment=${equipment.join(',')}`)
    //   .then(res => res.json())
    //   .then(data => {
    //     setSchedule(data.schedule);
    //     setCheckedIn(Array(data.schedule.length).fill(false));
    //     setShowSchedule(true);
    //   });
    // For now, just show a placeholder
    setSchedule([]);
    setCheckedIn(Array(days).fill(false));
    setShowSchedule(true);
  }

  function handleCheckIn(idx) {
    setCheckedIn(prev => prev.map((v, i) => i === idx ? !v : v));
  }

  function handleReset() {
    setShowSchedule(false);
    setSchedule([]);
    setEquipment(['None']);
    setDays(3);
    setCheckedIn([]);
    setGoal('');
    setShowGoalScreen(true);
  }

  return (
    <div className="workout-app">
      {showGoalScreen ? (
        <div className="goal-screen">
          <h1>Fitness Goals</h1>
          <div className="goal-options">
            <button className="goal-btn" onClick={() => handleGoalSelect('Build Muscle')}>💪 Build Muscle</button>
            <button className="goal-btn" onClick={() => handleGoalSelect('Burn Fat')}>🔥 Burn Fat</button>
            <button className="goal-btn" onClick={() => handleGoalSelect('General Fitness')}>🏃 General Fitness</button>
            <button className="goal-btn" onClick={() => handleGoalSelect('Increase Endurance')}>⏱️ Increase Endurance</button>
          </div>
        </div>
      ) : !showSchedule ? (
        <form className="setup-form" onSubmit={handleSubmit}>
          <h1>🏋️ Workout Split Planner</h1>
          <div className="goal-summary">Goal: <b>{goal}</b></div>
          <label>
            Days per week:
            <input
              type="number"
              min="1"
              max="7"
              value={days}
              onChange={e => setDays(Number(e.target.value))}
              required
            />
          </label>
          <fieldset>
            <legend>Select available equipment:</legend>
            <div className="equipment-options">
              {ALL_EQUIPMENT.map(eq => (
                <label key={eq} className="equipment-label">
                  <input
                    type="checkbox"
                    value={eq}
                    checked={equipment.includes(eq)}
                    onChange={handleEquipmentChange}
                  />
                  {eq}
                </label>
              ))}
            </div>
          </fieldset>
          <button type="submit">Generate Split Routine</button>
        </form>
      ) : (
        <div className="schedule-section">
          <h2>Your Weekly Split</h2>
          {schedule.length === 0 ? (
            <div style={{color: '#888', margin: '16px 0'}}>Your personalized split will appear here after backend integration.</div>
          ) : (
            <ul className="schedule-list">
              {schedule.map((split, idx) => (
                <li key={idx} className={checkedIn[idx] ? 'checked-in' : ''}>
                  {/* Render split/exercise info from backend here */}
                  <div>
                    <strong>{split.title}</strong>
                    <div><em>Approx. Duration:</em> {split.duration}</div>
                    <ul style={{margin: '8px 0 0 0', paddingLeft: '18px'}}>
                      {split.exercises.map((ex, i) => (
                        <li key={i}>
                          <b>{ex.name}</b> - {ex.duration}<br/>
                          <span style={{fontSize: '0.95em'}}>{ex.desc}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                  <button onClick={() => handleCheckIn(idx)}>
                    {checkedIn[idx] ? '✅ Checked In' : 'Check In'}
                  </button>
                </li>
              ))}
            </ul>
          )}
          <button onClick={handleReset} style={{marginTop: '18px'}}>Start Over</button>
        </div>
      )}
      <footer>
        <small>Front-end only: All split/exercise data will come from your Python backend. Edit this file to adjust UI only.</small>
      </footer>
    </div>
  );
}

// Mount the App component to the root div (front-end only)
ReactDOM.createRoot(document.getElementById('root')).render(<App />);
