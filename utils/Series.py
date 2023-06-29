import pandas as pd



class Series:
    def __init__(self, config) -> None:
        self.A0 = config["A0"]
        self.K0 = config["K0"]
        self.L0 = config["L0"]
        self.Y0 = config["Y0"]
        self.n = config["n"]
        self.alpha = config["alpha"]
        self.beta = 1 - config["alpha"]
        self.depreciation = config["depreciation"]
        self.pop_growth = config["pop_growth"]
        self.savings = config["savings"]
        self.innovation = config["innovation"]

        self.gdp = pd.DataFrame()
        self.gdp_pc = pd.DataFrame()

    def createDataset(self):
        gdp = pd.DataFrame.from_records([
            {
                't': 0,
                'A': self.A0,
                'L': self.L0,
                'K': self.K0,
                'Y': self.Y0,
            }
        ])

        for i in range(100):

            A_pt = gdp.iloc[i]['A']
            L_pt = gdp.iloc[i]['L']
            K_pt = gdp.iloc[i]['K']
            Y_pt = gdp.iloc[i]['Y']

            A_t = (1+self.innovation) * A_pt
            K_t = (1-self.depreciation) * K_pt + self.savings * Y_pt
            L_t = (1+self.pop_growth) * L_pt
            Y_t = (K_t)**self.alpha * (A_t * L_t)**self.beta

            gdp_t = pd.DataFrame.from_records([
                {
                    't': i,
                    'A': A_t,
                    'K': K_t,
                    'L': L_t,
                    'Y': Y_t
                },
            ])

            gdp = pd.concat([
                gdp,
                gdp_t
            ])
    

        self.gdp = gdp
        return self

    def print(self):
        print(self.gdp.to_string())
        return self

    def plot(self):
        x = self.gdp["t"]
        y = self.gdp["Y"]
        print(x, y)
        pd.DataFrame.plot(x, y)
        return self


