from pydantic import BaseModel

class Report(BaseModel):
    store_id: int
    uptime_last_hour: float
    uptime_last_day: float
    uptime_last_week: float
    downtime_last_hour: float
    downtime_last_day: float
    downtime_last_week: float
