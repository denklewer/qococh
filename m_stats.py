import json
import itertools

g_ship_hours = []
g_incr_hours = []

debug = True


changed_data2 = """
{
	"посылка 1": {
		"old": [
		{
			"id": "20181116_brown-ladybug-6",
			"dep_station": "GOT",
			"actual_arr_station": "HEL"
		},
		{
			"id": "20181112_itchy-lion-83",
			"dep_station": "HEL",
			"actual_arr_station": "KBP"
		}],
		"new": [
		{
			"id": "20181116_yellow-gecko-53_A",
			"dep_station": "GOT",
			"actual_arr_station": "ARN"
		},
		{
			"id": "20181116_modern-goose-66",
			"dep_station": "ARN",
			"actual_arr_station": "HEL"
		},
		{
			"id": "20181112_itchy-lion-83",
			"dep_station": "HEL",
			"actual_arr_station": "KBP"
		}],
		"prev_overall_time": "12",
		"cur_overall_time": "23.435"
	}
}
"""


def count_avg_time(changes):
	for shipment in changes:
		g_ship_hours.append(float(changes[shipment]['cur_overall_time']))
		g_incr_hours.append(float(changes[shipment]['cur_overall_time']) - float(changes[shipment]['prev_overall_time']))

	return sum(g_ship_hours) / len(g_ship_hours), sum(g_incr_hours) / len(g_incr_hours)


def recalculate_stats(changed_data):
	if debug:
		changed_data = json.loads(changed_data2)

	old_e = list(itertools.chain.from_iterable([changed_data[i]['old'] for i in changed_data]))
	new_e = list(itertools.chain.from_iterable([changed_data[i]['new'] for i in changed_data]))
	old_e = [i for i in old_e if i not in new_e]

	avg_h, avg_i = count_avg_time(changed_data)
	stats = {
		"avg_h": avg_h,
		"avg_i": avg_i
	}

	return old_e, new_e, stats
