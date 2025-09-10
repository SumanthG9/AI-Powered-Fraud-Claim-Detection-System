// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    claim_amount: '',
    age: '',
    gender: 'Male',
    location_policyholder: 'Mumbai',
    location_hospital: 'Mumbai',
    procedure_code: 'P101'
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError('');

    // Construct the payload with correct data types
    const payload = {
        ...formData,
        claim_amount: parseFloat(formData.claim_amount),
        age: parseInt(formData.age, 10)
    };
    
    try {
      const response = await axios.post('http://localhost:8000/predict', payload);
      setResult(response.data);
    } catch (err) {
      setError('An error occurred. Make sure the backend API is running.');
      console.error(err);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Star Health - AI Claim Fraud Detection</h1>
      </header>
      <main>
        <form onSubmit={handleSubmit} className="claim-form">
          <div className="form-group">
            <label>Claim Amount (₹)</label>
            <input type="number" name="claim_amount" value={formData.claim_amount} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Policyholder Age</label>
            <input type="number" name="age" value={formData.age} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Gender</label>
            <select name="gender" value={formData.gender} onChange={handleChange}>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
          <div className="form-group">
            <label>Policyholder Location</label>
            <input type="text" name="location_policyholder" value={formData.location_policyholder} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Hospital Location</label>
            <input type="text" name="location_hospital" value={formData.location_hospital} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Procedure Code</label>
            <select name="procedure_code" value={formData.procedure_code} onChange={handleChange}>
              <option value="P101">P101</option>
              <option value="P102">P102</option>
              <option value="P201">P201</option>
              <option value="P202">P202</option>
              <option value="P301">P301 (High Risk)</option>
              <option value="P302">P302 (High Risk)</option>
            </select>
          </div>
          <button type="submit">Analyze Claim</button>
        </form>

        {result && (
          <div className="result-container">
            <h2>Analysis Result</h2>
            <div className={`result-box ${result.is_fraudulent ? 'fraud' : 'legit'}`}>
              <p>Fraudulent Claim: <strong>{result.is_fraudulent ? 'Yes' : 'No'}</strong></p>
              <p>Fraud Probability: <strong>{(result.fraud_probability * 100).toFixed(2)}%</strong></p>
            </div>
          </div>
        )}
        {error && <p className="error-message">{error}</p>}
      </main>
    </div>
  );
}

export default App;