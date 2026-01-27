import { useState, useEffect } from 'react'

function App() {
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchSuggestions = async () => {
    try {
      setLoading(true);
      // Match the IP in your error log exactly
      const response = await fetch('http://127.0.0.1:8000/suggest');
      const data = await response.json();
      setSuggestions(data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching data:", error);
      setLoading(false);
    }
  };

  useEffect(() => { fetchSuggestions(); }, []);

  const styles = {
    container: {
      backgroundColor: '#121212',
      color: '#ffffff',
      minHeight: '100vh',
      padding: '60px 20px',
      fontFamily: 'Inter, system-ui, sans-serif',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    },
    tableContainer: {
      width: '100%',
      maxWidth: '1000px',
      border: '1px solid #333',
      borderRadius: '8px',
      backgroundColor: '#1a1a1a',
      overflow: 'hidden'
    },
    table: { width: '100%', borderCollapse: 'collapse' },
    th: {
      textAlign: 'left',
      padding: '16px',
      borderBottom: '1px solid #333',
      color: '#888',
      fontSize: '14px',
      fontWeight: '400'
    },
    td: {
      padding: '16px',
      borderBottom: '1px solid #2a2a2a',
      fontSize: '14px',
      color: '#e0e0e0'
    },
    refreshBtn: {
      marginTop: '30px',
      padding: '8px 24px',
      backgroundColor: '#2a2a2a',
      color: 'white',
      border: '1px solid #444',
      borderRadius: '6px',
      cursor: 'pointer'
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={{ fontSize: '64px', fontWeight: '400', margin: '0' }}>Catchup!</h1>
      <p style={{ color: '#666', fontSize: '20px', marginBottom: '40px' }}>Here are your suggestions for this week</p>

      <div style={styles.tableContainer}>
        <table style={styles.table}>
          <thead>
            <tr>
              <th style={styles.th}>Name</th>
              <th style={styles.th}>Contact Type</th>
              <th style={styles.th}>Local</th>
              <th style={styles.th}>Most Recent Contact</th>
            </tr>
          </thead>
          <tbody>
            {!loading && suggestions.map((friend, index) => (
              <tr key={index}>
                <td style={styles.td}>{friend.name}</td>
                <td style={styles.td}>{friend.contact_type}</td>
                <td style={styles.td}>{friend.local === 1 ? '1' : '0'}</td>
                <td style={styles.td}>{friend.most_recent_contact}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {loading && <p style={{ textAlign: 'center', padding: '20px', color: '#666' }}>Updating suggestions...</p>}
      </div>

      <button style={styles.refreshBtn} onClick={fetchSuggestions}>Refresh</button>
    </div>
  );
}

export default App;