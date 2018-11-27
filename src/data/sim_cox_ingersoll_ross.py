import numpy as np
import pandas as pd


def target_cpa_from_roas_error(cost_today, cost_range_i, revenue_today, revenue_range_i, current_target_cpa,
                               max_delta_cpa_pct, target_roas, weight_p):
    """
    Control algorithm of Proportional-Integral (PI) type. The algo uses bidding target CPA to adjust for deviation
    between target ROAS and realized ROAS at Bucket level.

    Steps:

        - Determine admissible target CPA range
        - Evaluate unscaled target CPA delta
        - Scale target CPA delta
        - Clip deltas outside admissible range

    :param cost_today:
    :param cost_range_i:
    :param revenue_today:
    :param revenue_range_i:
    :param current_target_cpa:
    :param max_delta_cpa_pct:
    :param target_roas:
    :param weight_p:
    :return: delta_target_cpa_clipped
    """

    assert cost_today.index.equals(cost_range_i.index)
    assert cost_range_i.index.equals(revenue_today.index)
    assert revenue_today.index.equals(revenue_range_i.index)

    # Determine admissible target CPA range

    max_delta_cpa_currency = current_target_cpa * max_delta_cpa_pct

    # Evaluate unscaled target CPA delta

    roas = pd.concat([revenue_today/cost_today, revenue_range_i/cost_range_i], axis=1)
    roas_err = roas - target_roas

    roas_err = roas_err.fillna(0)  # anomalies: NaN
    roas_err[(roas_err == -np.inf) | (roas_err == np.inf)] = 0  # anomalies: -inf, inf

    delta_target_cpa_unscaled = roas_err.dot([weight_p, 1-weight_p])

    # Scale target CPA delta

    max_delta_target_cpa_error_tolerance = 0.5
    delta_scaling = delta_target_cpa_unscaled / max_delta_target_cpa_error_tolerance
    delta_target_cpa_scaled = delta_scaling * max_delta_cpa_currency

    assert max_delta_cpa_currency.isna().sum() == 0   # no NaNs allowed - causes clipping to deactivate
    assert delta_target_cpa_scaled.isna().sum() == 0  # no NaNs allowed - causes clipping to deactivate

    # Clip deltas outside admissible range

    delta_target_cpa_clipped = delta_target_cpa_scaled.clip(-max_delta_cpa_currency, max_delta_cpa_currency)

    return delta_target_cpa_clipped
