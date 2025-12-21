def make_car(maker, model, **car_info):
    car_info["brand"] = maker
    car_info["model"] = model
    return car_info

print(make_car("honda", "civic", color="metal", type="sedan"))

