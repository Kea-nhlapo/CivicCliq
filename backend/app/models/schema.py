from pydantic import BaseModel
from typing import List, Optional

class MunicipalReport(BaseModel):
    title: str
    description: str
    location: str
    evidence_notes: str
    priority: str
    suggested_department: str

class CivicReportResponse(BaseModel):
    issue_type: str
    severity: str
    confidence: float
    summary: str
    responsible_department: str
    recommended_action: str
    municipal_report: MunicipalReport
    citizen_message: str
    next_steps: List[str]
