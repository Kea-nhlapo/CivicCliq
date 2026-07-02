import os
import json
import google.generativeai as genai
from PIL import Image
import io

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

    async def analyze_civic_issue(self, image_bytes: bytes, location: str, notes: str):
        if not self.model:
            return self._get_fallback_data(location, notes)

        prompt = f"""
        Analyze this civic infrastructure issue photo.
        Context: Location: {location}, User Notes: {notes}
        
        Provide a detailed analysis in strict JSON format with these fields:
        issue_type, severity (Low, Medium, High, Critical), confidence (0.0-1.0),
        summary, responsible_department, recommended_action, 
        municipal_report (title, description, location, evidence_notes, priority, suggested_department),
        citizen_message, next_steps (list).
        
        The report must be professional and formal.
        """
        
        try:
            img = Image.open(io.BytesIO(image_bytes))
            response = self.model.generate_content([prompt, img])
            # Clean JSON from response (remove ```json ... ```)
            clean_json = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(clean_json)
        except Exception as e:
            print(f"Gemini Error: {e}")
            return self._get_fallback_data(location, notes)

    def _get_fallback_data(self, location, notes):
        return {
            "issue_type": "Pothole (Demo)",
            "severity": "High",
            "confidence": 0.85,
            "summary": "Potential road hazard detected. This requires immediate inspection.",
            "responsible_department": "Public Works",
            "recommended_action": "Schedule emergency road repair.",
            "municipal_report": {
                "title": "Incident Report: Road Surface Damage",
                "description": f"Damaged road surface reported. User notes: {notes or 'None'}",
                "location": location or "Unknown location",
                "evidence_notes": "Photographic evidence attached.",
                "priority": "High",
                "suggested_department": "Public Works"
            },
            "citizen_message": "Report generated via Demo Mode. Please review before sending.",
            "next_steps": ["Verify location", "Submit to local council"]
        }
