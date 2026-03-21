from typing import Optional

from ..models import OptionContract, OptionsChainSnapshot


def choose_contract(action: str, chain: OptionsChainSnapshot) -> Optional[OptionContract]:
    if action == 'SELL_CE_ALERT':
        return chain.selected_ce
    if action == 'SELL_PE_ALERT':
        return chain.selected_pe
    return None
