"""
Question 2: Nearest Driver
@author: Aryan Ahadinia
"""

def updated_drivers(drivers_near: dict, served_driver: str,
                    served_cutomer: str) -> dict:
    driver_record = drivers_near['waiting'][served_driver]
    driver_record.append(served_cutomer)
    del drivers_near['waiting'][served_driver]
    drivers_near['working'][served_driver] = driver_record
    return drivers_near


def updated_request(req) -> dict:
    req['status'] = 'served'
    return req


def eucliducian_distance(p1: list, p2: list) -> int:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def get_distance(driver_record: dict, req: dict) -> dict:
    return eucliducian_distance(driver_record, req['location'])


def find_nearest_driver(delivery_request: dict, driver_near: dict) -> tuple:
    nearest = ''
    nearest_distance = 1000000000
    for k in driver_near['waiting']:
        distance = get_distance(driver_near['waiting'][k], delivery_request)
        if distance < nearest_distance:
            nearest = k
            nearest_distance = distance
    return updated_request(delivery_request), updated_drivers(
        driver_near, nearest, delivery_request['customer_id'])
