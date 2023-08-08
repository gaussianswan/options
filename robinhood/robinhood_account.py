import os 
import pandas as pd 
import robin_stocks 
import robin_stocks.robinhood as rs

from dotenv import load_dotenv

class RobinHoodAccount: 

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

        rs.login(
            username=username, 
            password=password
        )

        self.account_information = rs.build_user_profile() 
        self.holdings = rs.build_holdings()

    def get_options_portfolio(self) -> pd.DataFrame: 

        option_positions = rs.get_open_option_positions()
        option_position_df = pd.DataFrame.from_records(option_positions)
        option_position_df.set_index('option_id', inplace=True)

        cols = ['average_price', 'chain_symbol', 'type', 'quantity', 'trade_value_multiplier']
        condensed_options_data = option_position_df[cols]

        # Getting the market data on each of the options in our portfolio
        option_market_data = [] 
        for option_id in condensed_options_data.index: 
            data = rs.get_option_market_data_by_id(
                id = option_id
            )

            option_market_data = option_market_data + data

        option_market_data_df = pd.DataFrame.from_records(option_market_data).set_index('instrument_id')
        option_data_cols = ['adjusted_mark_price', 'break_even_price', 'volume', 'delta', 'gamma', 'implied_volatility', 'rho', 'theta', 'vega']
        portfolio_option_market_data = option_market_data_df[option_data_cols]

        # Changing the values to float
        portfolio_option_market_data = portfolio_option_market_data.astype(float)
        options_portfolio_df = condensed_options_data.merge(portfolio_option_market_data, left_index = True, right_index = True)

        options_portfolio_df['position_side'] = options_portfolio_df['type'].apply(lambda x: 1 if x == 'long' else -1)
        options_portfolio_df['quantity'] = options_portfolio_df['quantity'].astype(float)
        options_portfolio_df['trade_value_multiplier'] = options_portfolio_df['trade_value_multiplier'].astype(float)

        options_portfolio_df['position_delta'] = options_portfolio_df['delta'] * options_portfolio_df['quantity'] * options_portfolio_df['trade_value_multiplier'] * options_portfolio_df['position_side']
        options_portfolio_df['position_gamma'] = options_portfolio_df['gamma'] * options_portfolio_df['quantity'] * options_portfolio_df['trade_value_multiplier'] * options_portfolio_df['position_side']
        options_portfolio_df['position_theta'] = options_portfolio_df['theta'] * options_portfolio_df['quantity'] * options_portfolio_df['trade_value_multiplier'] * options_portfolio_df['position_side']
        options_portfolio_df['position_rho'] = options_portfolio_df['rho'] * options_portfolio_df['quantity'] * options_portfolio_df['trade_value_multiplier'] * options_portfolio_df['position_side']
        options_portfolio_df['position_vega'] = options_portfolio_df['vega'] * options_portfolio_df['quantity'] * options_portfolio_df['trade_value_multiplier'] * options_portfolio_df['position_side']
        
        return options_portfolio_df

    def get_options_portfolio_greeks(self) -> pd.DataFrame: 

        options_portfolio_df = self.get_options_portfolio() 

        greeks_report = options_portfolio_df.groupby('chain_symbol').sum()[['position_delta', 'position_gamma', 'position_theta', 'position_vega']].round(2)
        return greeks_report
    
    @classmethod 
    def from_dotenv_file(cls, dotenv_path: str = None): 
        """Class method for instantiating your robinhood account object from a dotenv file path

        Args:
            dotenv_path (str, optional): Path to your dotenv file. If you do not supply a path, the default path of None is used. This looks for a .env file 
            in your home directory. Defaults to None.

        Returns:
            _type_: _description_
        """

        load_dotenv(dotenv_path=dotenv_path)

        username = os.environ['ROBINHOOD_USERNAME']
        password = os.environ['ROBINHOOD_PASSWORD']
        return cls(username, password)


if __name__ == "__main__": 
    dotenv_path = './.env'
    robinhood_account = RobinHoodAccount.from_dotenv_file(dotenv_path=dotenv_path)
    print(robinhood_account.get_options_portfolio_greeks())

    