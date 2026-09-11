from typing import Dict, Any, List
import hashlib

class ProcurementFraudEngine:
    @staticmethod
    def audit_tender_bids(tender_id: str, bid_prices: List[float]) -> Dict[str, Any]:
        if not bid_prices or len(bid_prices) < 2:
            return {"fairness_score": 100.0, "status": "PASSED", "recommendations": ["Insufficient bids for variance analysis."]}
            
        avg_price = sum(bid_prices) / len(bid_prices)
        variance = sum((p - avg_price) ** 2 for p in bid_prices) / len(bid_prices)
        std_dev = variance ** 0.5
        cv = std_dev / max(avg_price, 1.0)
        
        is_suspicious = cv < 0.05
        fairness_score = 45.0 if is_suspicious else 95.0
        status = "FLAGGED_PRICE_COLLUSION" if is_suspicious else "PASSED_ETHICAL_AUDIT"
        
        hash_input = f"{tender_id}:{bid_prices}:{fairness_score}".encode()
        sha256_hash = hashlib.sha256(hash_input).hexdigest()
        
        recs = [
            "Identical bidding margins detected across multiple suppliers. Trigger mandatory audit." if is_suspicious 
            else "Bid distribution satisfies statutory procurement fairness standards."
        ]
        
        return {
            "fairness_score": fairness_score,
            "status": status,
            "sha256_hash": sha256_hash,
            "recommendations": recs
        }
