import React, { useState } from 'react';

export function TenderAuditForm({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [tenderId, setTenderId] = useState('TENDER-ETH-2026-88');
  const [prices, setPrices] = useState('500000, 502000, 501500');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      tender_id: tenderId,
      bid_prices: prices.split(',').map(p => Number(p.trim()))
    });
  };

  return (
    <form onSubmit={handleSubmit} style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0', marginBottom: '1.5rem' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>⚖️ Tender Fraud & Collusion Intake</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Tender Reference ID</label>
          <input value={tenderId} onChange={e => setTenderId(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Submitted Bid Prices (Comma-separated ETB)</label>
          <input value={prices} onChange={e => setPrices(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#dc2626', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Run Ethical Audit Engine
      </button>
    </form>
  );
}
