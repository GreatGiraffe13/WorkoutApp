// CATEGORY_OPTIONS and ALL_EQUIPMENT moved outside App for global access
const ALL_EQUIPMENT = ['None', 'Dumbbell', 'Resistance Bands', 'Barbells', 'Kettlebells', 'Complete Gym'];
const CATEGORY_OPTIONS = [
  { tag: 'Strength', emoji: '💪' },
  { tag: 'Cardio', emoji: '🏃' },
  { tag: 'Endurance', emoji: '⏱️' },
  { tag: 'Wellness', emoji: '🧘' },
  { tag: 'Other', emoji: '🌟' }
];

// Main React component for the Workout App (Front-End Only)

function App() {
  const [goal, setGoal] = React.useState('');
  const [showGoalScreen, setShowGoalScreen] = React.useState(true);
  const [days, setDays] = React.useState(3);
  const [equipment, setEquipment] = React.useState(['None']);
  const [schedule, setSchedule] = React.useState([]);
  const [showSchedule, setShowSchedule] = React.useState(false);
  const [checkedIn, setCheckedIn] = React.useState([]);
  const [activeTab, setActiveTab] = React.useState('fitfolio');
  const [achievements, setAchievements] = React.useState([]);
  const [showAddAchievement, setShowAddAchievement] = React.useState(false);
  const [newAchievement, setNewAchievement] = React.useState({
    title: '',
    reflection: '',
    date: new Date().toISOString().slice(0, 10),
    category: '',
    emoji: '',
    photo: null,
    photoURL: '',
    mood: 3
  });
  const [dashboardMood, setDashboardMood] = React.useState([]);
  const [revealMilestone, setRevealMilestone] = React.useState(null);
  const [showLockScreen, setShowLockScreen] = React.useState(true);
  const [lockAchievement, setLockAchievement] = React.useState(null);
  const [clock, setClock] = React.useState(new Date());

  React.useEffect(() => {
    if (showLockScreen) {
      const interval = setInterval(() => setClock(new Date()), 1000);
      return () => clearInterval(interval);
    }
  }, [showLockScreen]);

  function handleEquipmentChange(e) {
    const value = e.target.value;
    setEquipment(prev => {
      if (value === 'None') return ['None'];
      const withoutNone = prev.filter(eq => eq !== 'None');
      return prev.includes(value)
        ? withoutNone.filter(eq => eq !== value)
        : [...withoutNone, value];
    });
  }

  function handleGoalSelect(selectedGoal) {
    setGoal(selectedGoal);
    setShowGoalScreen(false);
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (equipment.length === 0) {
      alert("Please select at least one equipment option.");
      return;
    }
    setSchedule([]); // Placeholder, integrate backend later
    setCheckedIn(Array(days).fill(false));
    setShowSchedule(true);
  }

  function handleCheckIn(idx) {
    setCheckedIn(prev => prev.map((v, i) => (i === idx ? !v : v)));
  }

  function handleReset() {
    setActiveTab('planner');
    setShowSchedule(false);
    setSchedule([]);
    setEquipment(['None']);
    setDays(3);
    setCheckedIn([]);
    setGoal('');
    setShowGoalScreen(true);
  }

  function handleAddAchievement(e) {
    e.preventDefault();
    if (!newAchievement.title) return;
    const cat = CATEGORY_OPTIONS.find(c => c.tag === newAchievement.category) || CATEGORY_OPTIONS[4];
    const ach = {
      ...newAchievement,
      id: Date.now(),
      likes: 0,
      comments: [],
      emoji: cat.emoji,
      category: cat.tag
    };
    setRevealMilestone(ach);
    setTimeout(() => {
      setAchievements(prev => [ach, ...prev]);
      setDashboardMood(prev => [{ date: ach.date, mood: ach.mood }, ...prev]);
      setRevealMilestone(null);
    }, 3500);
    setNewAchievement({ title: '', reflection: '', date: new Date().toISOString().slice(0,10), category: '', emoji: '', photo: null, photoURL: '', mood: 3 });
    setShowAddAchievement(false);
  }

  function handlePhotoChange(e) {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = ev => setNewAchievement(a => ({ ...a, photo: file, photoURL: ev.target.result }));
      reader.readAsDataURL(file);
    }
  }

  function handleLike(id) {
    setAchievements(prev => prev.map(a => a.id === id ? { ...a, likes: a.likes + 1 } : a));
  }

  function handleComment(id, text) {
    setAchievements(prev => prev.map(a => a.id === id ? { ...a, comments: [...a.comments, text] } : a));
  }

  // Add handler to set lock screen achievement
  function handleSetLockAchievement(ach) {
    setLockAchievement(ach);
    setShowLockScreen(true);
  }

  // Animated Lock Screen
  if (showLockScreen) {
    // Use US Eastern Time for display
    const timeStr = clock.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'America/New_York' });
    const dateStr = clock.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric', timeZone: 'America/New_York' });
    const bg = lockAchievement && lockAchievement.photoURL ? `url(${lockAchievement.photoURL})` : 'linear-gradient(135deg, #e0e7ff 0%, #f6d365 100%)';
    return (
      <div className="lock-screen" style={{
        position: 'fixed', inset: 0, zIndex: 1000, background: bg, backgroundSize: 'cover', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', transition: 'background 0.8s', animation: 'fadeIn 1.2s', color: '#222', fontFamily: 'Nunito, sans-serif'
      }}>
        <div style={{ textAlign: 'center', marginBottom: 32, animation: 'slideDown 1s' }}>
          <div style={{ fontSize: 54, fontWeight: 700, letterSpacing: 2, textShadow: '0 2px 12px #fff8' }}>{timeStr} <span style={{fontSize:18, color:'#2563eb'}}>EST</span></div>
          <div style={{ fontSize: 20, color: '#2563eb', marginBottom: 12 }}>{dateStr}</div>
          <div style={{ fontSize: 22, fontWeight: 600, marginBottom: 8 }}>Welcome to your Fitfolio</div>
          {lockAchievement ? (
            <div style={{ margin: '18px 0', animation: 'fadeIn 1.2s 0.5s both' }}>
              <div style={{ fontSize: 32 }}>{lockAchievement.emoji}</div>
              <div style={{ fontWeight: 700, fontSize: 20 }}>{lockAchievement.title}</div>
              {lockAchievement.reflection && <div style={{ fontStyle: 'italic', color: '#3b3b5c', marginTop: 6 }}>{lockAchievement.reflection}</div>}
            </div>
          ) : (
            <div style={{ color: '#888', fontSize: 16, margin: '18px 0' }}>Set a favorite achievement as your lock screen!</div>
          )}
        </div>
        <button onClick={() => setShowLockScreen(false)} style={{ background: '#38b6ff', color: '#fff', borderRadius: 18, padding: '14px 38px', fontWeight: 700, fontSize: 20, boxShadow: '0 2px 12px rgba(56,182,255,0.18)', border: 'none', cursor: 'pointer', transition: 'background 0.3s', animation: 'fadeIn 1.2s 0.8s both' }}>Proceed</button>
      </div>
    );
  }

  return (
    <div className="workout-app" style={{ animation: 'fadeIn 1.2s' }}>
      <nav style={{ display: 'flex', justifyContent: 'center', gap: 18, marginBottom: 18 }}>
        <button onClick={() => setActiveTab('planner')} style={{ fontWeight: activeTab === 'planner' ? 'bold' : 'normal', transition: 'all 0.3s' }}>🏋️ Planner</button>
        <button onClick={() => setActiveTab('fitfolio')} style={{ fontWeight: activeTab === 'fitfolio' ? 'bold' : 'normal', transition: 'all 0.3s' }}>📖 Fitfolio</button>
        <button onClick={() => setActiveTab('dashboard')} style={{ fontWeight: activeTab === 'dashboard' ? 'bold' : 'normal', transition: 'all 0.3s' }}>📊 Dashboard</button>
      </nav>

      {revealMilestone ? (
        <MilestoneRevealCard milestone={revealMilestone} />
      ) : activeTab === 'planner' ? (
        showGoalScreen ? (
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
              <div style={{ color: '#888', margin: '16px 0' }}>Your personalized split will appear here after backend integration.</div>
            ) : (
              <ul className="schedule-list">
                {schedule.map((split, idx) => (
                  <li key={idx} className={checkedIn[idx] ? 'checked-in' : ''}>
                    <div>
                      <strong>{split.title}</strong>
                      <div><em>Approx. Duration:</em> {split.duration}</div>
                      <ul>
                        {split.exercises.map((ex, i) => (
                          <li key={`${ex.name}-${i}`}>
                            <b>{ex.name}</b> - {ex.duration}<br />
                            <span>{ex.desc}</span>
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
            <button onClick={handleReset} style={{ marginTop: '18px' }}>Start Over</button>
          </div>
        )
      ) : activeTab === 'fitfolio' ? (
        <div className="fitfolio-section" style={{ background: 'linear-gradient(135deg, #e0e7ff 0%, #f6d365 100%)', minHeight: 500, borderRadius: 18, padding: 0, animation: 'fadeInUp 0.8s' }}>
          <h1 style={{ textAlign: 'center', color: '#2563eb', fontWeight: 700, margin: '18px 0 12px 0' }}>Your Story Feed</h1>
          <div style={{ position: 'fixed', bottom: 32, right: 32, zIndex: 10 }}>
            <button onClick={() => setShowAddAchievement(true)} style={{ background: '#38b6ff', color: '#fff', borderRadius: '50%', width: 56, height: 56, fontSize: 32, boxShadow: '0 2px 12px rgba(56,182,255,0.18)', border: 'none', cursor: 'pointer', transition: 'background 0.3s, transform 0.2s', animation: 'popIn 0.7s' }}>+</button>
          </div>
          {showAddAchievement && (
            <form className="achievement-form" onSubmit={handleAddAchievement} style={{ background: '#fff', borderRadius: 16, maxWidth: 340, margin: '32px auto', padding: 24, boxShadow: '0 2px 12px rgba(56,182,255,0.10)' }}>
              <h2 style={{ color: '#2563eb', marginBottom: 12 }}>What did you achieve today?</h2>
              <input type="text" placeholder="Milestone (e.g. Ran 5k)" value={newAchievement.title} onChange={e => setNewAchievement(a => ({ ...a, title: e.target.value }))} required style={{ display: 'block', marginBottom: 10, width: '100%' }} />
              <select value={newAchievement.category} onChange={e => setNewAchievement(a => ({ ...a, category: e.target.value }))} style={{ display: 'block', marginBottom: 10, width: '100%' }}>
                <option value="">Tag (optional)</option>
                {CATEGORY_OPTIONS.map(opt => <option key={opt.tag} value={opt.tag}>{opt.emoji} {opt.tag}</option>)}
              </select>
              <input type="date" value={newAchievement.date} onChange={e => setNewAchievement(a => ({ ...a, date: e.target.value }))} style={{ display: 'block', marginBottom: 10, width: '100%' }} />
              <textarea placeholder="How did you feel? (Reflection)" value={newAchievement.reflection} onChange={e => setNewAchievement(a => ({ ...a, reflection: e.target.value }))} style={{ display: 'block', marginBottom: 10, width: '100%' }} />
              <input type="file" accept="image/*" onChange={handlePhotoChange} style={{ marginBottom: 10 }} />
              {newAchievement.photoURL && <img src={newAchievement.photoURL} alt="preview" style={{ maxWidth: 120, marginBottom: 10, borderRadius: 8 }} />}
              <label style={{ display: 'block', marginBottom: 10 }}>Mood: <input type="range" min="1" max="5" value={newAchievement.mood} onChange={e => setNewAchievement(a => ({ ...a, mood: Number(e.target.value) }))} /></label>
              <button type="submit" style={{ background: '#38b6ff', color: '#fff', borderRadius: 8, padding: '8px 18px', fontWeight: 600 }}>Post</button>
              <button type="button" onClick={() => setShowAddAchievement(false)} style={{ marginLeft: 8, background: '#eee', color: '#2563eb', borderRadius: 8, padding: '8px 18px', fontWeight: 600 }}>Cancel</button>
            </form>
          )}
          <div className="fitfolio-feed" style={{ maxWidth: 420, margin: '0 auto', padding: '0 0 80px 0', overflowY: 'auto' }}>
            {achievements.length === 0 ? (
              <div style={{ color: '#888', textAlign: 'center', marginTop: 32 }}>No milestones yet. Your story starts today!</div>
            ) : (
              achievements.map(a => (
                <div key={a.id} className="achievement-card" style={{ background: '#fff', borderRadius: 16, padding: 18, margin: '18px 0', boxShadow: '0 2px 12px rgba(56,182,255,0.10)', display: 'flex', flexDirection: 'column', gap: 8, animation: 'fadeInUp 0.7s' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                    <span style={{ fontSize: 24 }}>{a.emoji}</span>
                    <span style={{ color: '#2563eb', fontWeight: 600 }}>{a.category}</span>
                    <span style={{ marginLeft: 'auto', color: '#888', fontSize: '0.98em' }}>{a.date}</span>
                  </div>
                  <div style={{ fontWeight: 700, fontSize: '1.15em' }}>{a.title}</div>
                  {a.photoURL && <img src={a.photoURL} alt="milestone" style={{ width: '100%', maxWidth: 320, borderRadius: 10, margin: '8px 0' }} />}
                  {a.reflection && <div style={{ fontStyle: 'italic', color: '#3b3b5c', background: '#f1f5f9', borderRadius: 8, padding: 8 }}>{a.reflection}</div>}
                  <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginTop: 6 }}>
                    <button onClick={() => handleLike(a.id)} style={{ background: 'none', color: '#38b6ff', fontWeight: 600, border: 'none', cursor: 'pointer', transition: 'color 0.2s' }}>❤️ {a.likes}</button>
                    <button onClick={() => handleSetLockAchievement(a)} style={{ background: '#eee', color: '#2563eb', borderRadius: 8, padding: '4px 10px', fontWeight: 600, fontSize: 13, marginLeft: 8, border: 'none', cursor: 'pointer', transition: 'background 0.2s' }}>Set as Lock</button>
                  </div>
                  <div style={{ marginTop: 8 }}>
                    <CommentBox onComment={text => handleComment(a.id, text)} comments={a.comments} />
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      ) : (
        <Dashboard achievements={achievements} moodData={dashboardMood} />
      )}

      <footer>
        <small>Front-end only: All split/exercise data will come from your Python backend. Edit this file to adjust UI only.</small>
      </footer>
    </div>
  );
}

// Other components unchanged
// Paste your existing MilestoneRevealCard, CommentBox, and Dashboard components here

function MilestoneRevealCard({ milestone }) {
  const [typedTitle, setTypedTitle] = React.useState('');
  React.useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      setTypedTitle(milestone.title.slice(0, i + 1));
      i++;
      if (i >= milestone.title.length) clearInterval(interval);
    }, 60);
    return () => clearInterval(interval);
  }, [milestone.title]);
  return (
    <div className="reveal-overlay">
      <div className="confetti-bg"></div>
      <div className="reveal-card">
        <div className="reveal-emoji">{milestone.emoji}</div>
        <div className="reveal-date">{milestone.date}</div>
        <div className="reveal-title typewriter">{typedTitle}</div>
        {milestone.photoURL && <img src={milestone.photoURL} alt="milestone" className="reveal-photo" />}
        <div className="reveal-reflection pulse-glow">{milestone.reflection}</div>
      </div>
    </div>
  );
}

function CommentBox({ onComment, comments }) {
  const [text, setText] = React.useState('');
  return (
    <div style={{ background: '#f9fafb', borderRadius: 8, padding: 8 }}>
      <div style={{ marginBottom: 6, fontWeight: 600, color: '#2563eb' }}>Encouragement</div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, marginBottom: 6 }}>
        {comments.map((c, i) => <li key={i} style={{ fontSize: '0.98em', marginBottom: 2 }}>💬 {c}</li>)}
      </ul>
      <form onSubmit={e => { e.preventDefault(); if (text) { onComment(text); setText(''); } }} style={{ display: 'flex', gap: 6 }}>
        <input value={text} onChange={e => setText(e.target.value)} placeholder="Write a comment..." style={{ flex: 1, borderRadius: 6, border: '1px solid #ddd', padding: 6 }} />
        <button type="submit" style={{ background: '#38b6ff', color: '#fff', borderRadius: 6, padding: '6px 12px', fontWeight: 600 }}>Post</button>
      </form>
    </div>
  );
}

function Dashboard({ achievements, moodData }) {
  const now = new Date();
  const thisMonth = now.toISOString().slice(0, 7);
  const milestonesThisMonth = achievements.filter(a => a.date.startsWith(thisMonth)).length;
  const catCounts = CATEGORY_OPTIONS.reduce((acc, c) => ({ ...acc, [c.tag]: achievements.filter(a => a.category === c.tag).length }), {});
  const moodPoints = moodData.slice().reverse().map((m, i) => ({ x: i, y: m.mood }));
  return (
    <div className="dashboard-section" style={{ maxWidth: 420, margin: '0 auto', background: '#fff', borderRadius: 16, padding: 24, boxShadow: '0 2px 12px rgba(56,182,255,0.10)' }}>
      <h1 style={{ color: '#2563eb', textAlign: 'center', marginBottom: 18 }}>Progress Dashboard</h1>
      <div style={{ marginBottom: 18, fontWeight: 600 }}>Milestones this month: <span style={{ color: '#38b6ff' }}>{milestonesThisMonth}</span></div>
      <div style={{ marginBottom: 18 }}>
        <div style={{ fontWeight: 600, marginBottom: 6 }}>Categories:</div>
        <div style={{ display: 'flex', gap: 12 }}>
          {CATEGORY_OPTIONS.map(c => (
            <div key={c.tag} style={{ background: '#f1f5f9', borderRadius: 8, padding: '6px 12px', color: '#2563eb', fontWeight: 600, minWidth: 60, textAlign: 'center' }}>
              <span style={{ fontSize: 18 }}>{c.emoji}</span><br />{catCounts[c.tag] || 0}
            </div>
          ))}
        </div>
      </div>
      <div style={{ marginBottom: 18 }}>
        <div style={{ fontWeight: 600, marginBottom: 6 }}>Mood Over Time:</div>
        <div style={{ height: 60, background: '#f1f5f9', borderRadius: 8, display: 'flex', alignItems: 'flex-end', gap: 2, padding: 6 }}>
          {moodPoints.length === 0 ? <span style={{ color: '#bbb' }}>No data yet</span> :
            moodPoints.map((p, i) => (
              <div key={i} style={{ width: 8, height: `${p.y * 10 + 10}px`, background: '#38b6ff', borderRadius: 4, transition: 'height 0.3s' }} title={`Mood: ${p.y}`}></div>
            ))}
        </div>
        <div style={{ fontSize: '0.98em', color: '#888', marginTop: 4 }}>5 = Great, 1 = Tough</div>
      </div>
    </div>
  );
}

// Ensure this file has NO export or import statements and is pure JSX/JS for Babel in-browser.
// Add a fallback for React not loaded (for debugging in Live Server):
const rootElem = document.getElementById('root');
if (!rootElem) {
  document.body.innerHTML = '<div style="color:red;font-size:1.2em;padding:2em;text-align:center;">No <b>#root</b> element found. Make sure you are opening <b>Front end/index.html</b> in Live Server, not the project root or a folder.</div>';
} else if (typeof React === 'undefined' || typeof ReactDOM === 'undefined') {
  rootElem.innerHTML = '<div style="color:red;font-size:1.2em;padding:2em;text-align:center;">React or ReactDOM not loaded. Check your <b>index.html</b> script tags and reload.</div>';
} else {
  ReactDOM.createRoot(rootElem).render(<App />);
}
