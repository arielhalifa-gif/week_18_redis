from fastapi import FastAPI


app = FastAPI()

@app.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    pass



@app.get("/analytics/top-urgent-zones")
def top_urgent_zones():
    