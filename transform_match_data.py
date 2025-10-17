import pandas as pd
from json import loads
from constants import SERVER_NAMES


def transform_raw_match_data(df: pd.DataFrame):
    unpacked_info = pd.json_normalize(df['info'])
    df = pd.concat([df['match_id'], unpacked_info], axis="columns")
    df['region'] = df['match_id'].apply(lambda x: SERVER_NAMES[x.split('_')[0]])

    expanded = df.explode(column='participants', ignore_index=True)
    unpacked_player_record = pd.json_normalize(expanded['participants'])
    expanded.pop('participants')
    return pd.concat([expanded, unpacked_player_record], axis="columns")


def calculate_resource_totals(match_record):
    pass


def calc_unit_item_counts(unit_record: dict):
    return {
        'craftable': 0,
        'radiant': 0,
        'artifact': 0,
        'emblem': 0
    }

def calc_unit_shop_cost(unit_record: dict):
    return 0


my_df = pd.read_csv('data/match_data.csv', converters={"info": loads}, nrows=100)
transformed = transform_raw_match_data(my_df)

from pprint import pformat
print(pformat(transformed['units'][0], width = 200))
