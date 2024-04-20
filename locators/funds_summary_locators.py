FUNDS_SUMMARY = {
    'GENERIC_INFO_TAB': 'nav.navbar--funds li:nth-child(1)',
    'ASSETS_DISTRIBUTION_TAB': 'nav.navbar--funds li:nth-child(2)',
    'PROFITABILITY_TAB': 'nav.navbar--funds li:nth-child(3)',
    'COMMISSIONS_TAB': 'nav.navbar--funds li:nth-child(4)'
}

ASSETS_DISTRIBUTION_TAB = {
    'ALLOCATION': 'div.tabassets span.tabassets--allocation ',
    'EXPOSURE': 'div.tabassets div.tabassets--exposure ',
    'HOLDINGS': 'div.tabassets span.tabassets--holdings ',
    'CAPITAL': 'div.tabassets span.tabassets--capital '
}

SCRAP_TABLE = {
    'KEY': lambda column: f'table thead tr:nth-child(1) th:nth-child({column})',
    'VALUE': lambda row, column: f'table tbody tr:nth-child({row}) td:nth-child({column})'
}