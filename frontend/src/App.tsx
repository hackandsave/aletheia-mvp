// This is the main "room" of our application.
// Its only job is to display our QuestDashboard component.

import QuestDashboard from './components/QuestDashboard'; // Imports the dashboard we just built.

function App() {
  // The component just returns the dashboard, nothing else.
  return (
    <QuestDashboard />
  );
}

export default App; // Makes this main App component available.