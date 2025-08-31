// This file defines our main user interface component.
// We're using React with TypeScript, which is what the ".tsx" extension means.

import React from 'react'; // Imports the main React library.

// This is the main function that defines our component.
// It's like the blueprint for our "dining table."
const QuestDashboard = () => {
  // For the MVP, we'll start with some placeholder data.
  // In the next step, we'll replace this with real data from our backend.
  const activeQuest = "Design and implement a 30-minute morning routine.";
  const ifThenPlans = [
    { id: 1, text: "IF it is 7:00 AM, THEN I will meditate for 5 minutes." },
    { id: 2, text: "IF I finish meditating, THEN I will write one page in my journal." },
    { id: 3, text: "IF I finish journaling, THEN I will review my top priority for the day." },
  ];

  // This "return" section is what gets drawn on the screen.
  // It looks like HTML but is actually a syntax called JSX.
  return (
    <div style={{ fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto', padding: '2rem' }}>

      <header style={{ borderBottom: '2px solid #eee', paddingBottom: '1rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', margin: 0 }}>Aletheia</h1>
        <p style={{ margin: 0, color: '#555' }}>Your Personal Operating System</p>
      </header>

      <main>
        <section id="quest-section">
          <h2 style={{ fontSize: '1.2rem', color: '#333' }}>Active Quest:</h2>
          <p style={{ fontSize: '1.5rem', color: '#000', margin: '0.5rem 0' }}>
            {activeQuest}
          </p>
        </section>

        <section id="plans-section" style={{ marginTop: '3rem' }}>
          <h3 style={{ fontSize: '1.2rem', color: '#333' }}>If-Then Plans:</h3>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {ifThenPlans.map(plan => (
              <li key={plan.id} style={{ background: '#f9f9f9', padding: '1rem', border: '1px solid #ddd', borderRadius: '8px', marginBottom: '1rem' }}>
                {plan.text}
              </li>
            ))}
          </ul>
        </section>
      </main>

    </div>
  );
};

export default QuestDashboard; // This makes our component available to be used by other files.