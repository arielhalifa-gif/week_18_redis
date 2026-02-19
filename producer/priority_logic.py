import json
from redis_connection import RedisConnection as R

class Priority:

    @staticmethod
    def priority_logic():
        with open('data/border_alerts.json', 'r') as f:
            alerts = json.load(f)

        for alert in alerts:
            priority = 'NORMAL'
            if (alert['weapons_count'] > 0) or (alert['distance_from_fence_m'] <= 50) or (alert['people_count'] > 8) or (alert['vehicle_type'] == 'truck'):
                priority = 'URGENT'
            elif (alert['people_count'] >= 4 and alert['distance_from_fence_m'] <= 50) or (alert['people_count'] <= 3 and alert['vehicle_type'] == 'jeep'):
                priority = 'URGENT'
            alert['priority'] = priority
        for alert in alerts:
            if alert['priority'] == 'URGENT':
                R.redis_queue_priority(alert, 'queue_urgent')
            else:
                R.redis_queue_priority(alert, 'queue_normal')
        return "data send by priority order"