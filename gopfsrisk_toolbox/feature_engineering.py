# feature engineering
import numpy as np
import time

# create fe class
class FeatureEngineeringAaronPDLGDLower:
	# transform
	def transform(self, X):
		time_start = time.perf_counter()
		# from James
		# down payment to amount financed
		try:
			X['eng_down_to_financed'] = X['fltapproveddowntotal__app'] / X['fltamountfinanced__app']
		except:
			pass
		# down payment over gross monthly
		try:
			X['eng_down_to_income'] = X['fltapproveddowntotal__app'] / X['fltgrossmonthly__income_sum']
		except:
			pass
		# down payment to price wholesale
		try:
			X['eng_down_to_wholesale'] = X['fltapproveddowntotal__app'] / X['fltapprovedpricewholesale__app']
		except:
			pass
		# Cyclic: Month relative to year
		# sin
		try:
			X['eng_applicationmonth__app_sin'] = np.sin((X['applicationmonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# cos
		try:
			X['eng_applicationmonth__app_cos'] = np.cos((X['applicationmonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# tan
		try:
			X['eng_applicationmonth__app_tan'] = X['eng_applicationmonth__app_sin'] / X['eng_applicationmonth__app_cos']
		except:
			pass
		# Cyclic: Quarter relative to year
		# sin
		try:
			X['eng_applicationquarter__app_sin'] = np.sin((X['applicationquarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# cos
		try:
			X['eng_applicationquarter__app_cos'] = np.cos((X['applicationquarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# tan
		try:
			X['eng_applicationquarter__app_tan'] = X['eng_applicationquarter__app_sin'] / X['eng_applicationquarter__app_cos']
		except:
			pass
		# loan to value
		try:
			X['eng_loan_to_value'] = X['fltamountfinanced__app'] / X['fltapprovedpricewholesale__app']
		except:
			pass
		# debt to income
		try:
			X['eng_debt_to_income'] = X['fltmonthlypayment__debt_mean'] / X['fltgrossmonthly__income_sum']
		except:
			pass
		print(f'Time to feature engineer: {(time.perf_counter()-time_start):0.5} sec.')
		# return
		return X

# create fe class
class FeatureEngineeringAaronPD:
	# transform
	def transform(self, X):
		time_start = time.perf_counter()
		# from James
		# down payment to amount financed
		try:
			X['ENG_down_to_financed'] = X['fltApprovedDownTotal__app'] / X['fltAmountFinanced__app']
		except:
			pass
		# down payment over gross monthly
		try:
			X['ENG_down_to_income'] = X['fltApprovedDownTotal__app'] / X['fltGrossMonthly__income_sum']
		except:
			pass
		# down payment to price wholesale
		try:
			X['ENG_down_to_wholesale'] = X['fltApprovedDownTotal__app'] / X['fltApprovedPriceWholesale__app']
		except:
			pass
		# Cyclic: Month relative to year
		# sin
		try:
			X['ENG_ApplicationMonth__app_sin'] = np.sin((X['ApplicationMonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# cos
		try:
			X['ENG_ApplicationMonth__app_cos'] = np.cos((X['ApplicationMonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# tan
		try:
			X['ENG_ApplicationMonth__app_tan'] = X['ENG_ApplicationMonth__app_sin'] / X['ENG_ApplicationMonth__app_cos']
		except:
			pass
		# Cyclic: Quarter relative to year
		# sin
		try:
			X['ENG_ApplicationQuarter__app_sin'] = np.sin((X['ApplicationQuarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# cos
		try:
			X['ENG_ApplicationQuarter__app_cos'] = np.cos((X['ApplicationQuarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# tan
		try:
			X['ENG_ApplicationQuarter__app_tan'] = X['ENG_ApplicationQuarter__app_sin'] / X['ENG_ApplicationQuarter__app_cos']
		except:
			pass
		# loan to value
		try:
			X['ENG_loan_to_value'] = X['fltAmountFinanced__app'] / X['fltApprovedPriceWholesale__app']
		except:
			pass
		# debt to income
		try:
			X['ENG_debt_to_income'] = X['fltMonthlyPayment__debt_mean'] / X['fltGrossMonthly__income_sum']
		except:
			pass
		print(f'Time to feature engineer: {(time.perf_counter()-time_start):0.5} sec.')
		# return
		return X

# create fe class
class FeatureEngineeringAaronLGD:
	# transform
	def transform(self, X):
		time_start = time.perf_counter()
		# from James
		# down payment to amount financed
		try:
			X['ENG_down_to_financed'] = X['fltApprovedDownTotal__app'] / X['fltAmountFinanced__app']
		except:
			pass
		# down payment over gross monthly
		try:
			X['ENG_down_to_income'] = X['fltApprovedDownTotal__app'] / X['fltGrossMonthly__income_sum']
		except:
			pass
		# down payment to price wholesale
		try:
			X['ENG_down_to_wholesale'] = X['fltApprovedDownTotal__app'] / X['fltApprovedPriceWholesale__app']
		except:
			pass
		# Cyclic: Month relative to year
		# sin
		try:
			X['ENG_ApplicationMonth__app_sin'] = np.sin((X['ApplicationMonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# cos
		try:
			X['ENG_ApplicationMonth__app_cos'] = np.cos((X['ApplicationMonth__app']-1) * (2*np.pi/12))
		except:
			pass
		# tan
		try:
			X['ENG_ApplicationMonth__app_tan'] = X['ENG_ApplicationMonth__app_sin'] / X['ENG_ApplicationMonth__app_cos']
		except:
			pass
		# Cyclic: Quarter relative to year
		# sin
		try:
			X['ENG_ApplicationQuarter__app_sin'] = np.sin((X['ApplicationQuarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# cos
		try:
			X['ENG_ApplicationQuarter__app_cos'] = np.cos((X['ApplicationQuarter__app']-1) * (2*np.pi/4))
		except:
			pass
		# tan
		try:
			X['ENG_ApplicationQuarter__app_tan'] = X['ENG_ApplicationQuarter__app_sin'] / X['ENG_ApplicationQuarter__app_cos']
		except:
			pass
		# loan to value
		try:
			X['ENG_loan_to_value'] = X['fltAmountFinanced__app'] / X['fltApprovedPriceWholesale__app']
		except:
			pass
		# debt to income
		try:
			X['ENG_debt_to_income'] = X['fltMonthlyPayment__debt_mean'] / X['fltGrossMonthly__income_sum']
		except:
			pass
		print(f'Time to feature engineer: {(time.perf_counter()-time_start):0.5} sec.')
		# return
		return X

"""
class FeatureEngineeringAndrew:
    def __init__(self, bool_drop_feats=True):
        self.bool_drop_feats = bool_drop_feats
    # transform
    def transform(self,X):
        # removing pseudo-missing values (negatives) with NaN, collecting a mean, then imputing any completely missing with 0
        # deleting original columns afterwards
        # this takes a long time to complete
        try:
            X['balances'] = X.loc[:,'agg101__tuaccept':'agg124__tuaccept'].where(X.loc[:,'agg101__tuaccept':'agg124__tuaccept']>0,np.nan).apply(lambda x: np.nanmean(x), axis=1)
            X['balances'] = X['balances'].fillna(0)
            # here, create a list of features to drop
            if self.bool_drop_feats:
                for col in X.loc[:,'agg101__tuaccept':'agg124__tuaccept'].columns:
                    if col in list(X.columns):
                        del X[col]
        except:
            pass
        try:
            X['credit_line'] = X.loc[:,'agg201__tuaccept':'agg224__tuaccept'].where(X.loc[:,'agg201__tuaccept':'agg224__tuaccept']>0,np.nan).apply(lambda x: np.nanmean(x), axis=1)
            X['credit_line'] = X['credit_line'].fillna(0)
            # here, create a list of features to drop
            if self.bool_drop_feats:
                for col in X.loc[:,'agg201__tuaccept':'agg224__tuaccept'].columns:
                    if col in list(X.columns):
                        del X[col]
        except:
            pass
        try:
            X['amount_past_due'] = X.loc[:,'agg301__tuaccept':'agg324__tuaccept'].where(X.loc[:,'agg301__tuaccept':'agg324__tuaccept']>0,np.nan).apply(lambda x: np.nanmean(x), axis=1)
            X['amount_past_due'] = X['amount_past_due'].fillna(0)
            # here, create a list of features to drop
            if self.bool_drop_feats:
                for col in X.loc[:,'agg301__tuaccept':'agg324__tuaccept'].columns:
                    if col in list(X.columns):
                        del X[col]
        except:
            pass
        try:
            X['agg_spending'] = X.loc[:,'aggs101__tuaccept':'aggs124__tuaccept'].where(X.loc[:,'aggs101__tuaccept':'aggs124__tuaccept']>0,np.nan).apply(lambda x: np.nanmean(x), axis=1)
            X['balances'] = X['balances'].fillna(0)
            # here, create a list of features to drop
            if self.bool_drop_feats:
                for col in X.loc[:,'aggs101__tuaccept':'aggs124__tuaccept'].columns:
                    if col in list(X.columns):
                        del X[col]
        except:
            pass
        return X
"""