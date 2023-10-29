from zillow import ZillowRentalSearch

GOOGLE_FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLScIi4o8ikHPGDoPwnvwwo9nM-UcYL1rvDlfHUxTh8tsEY83IQ"
                   "/viewform?usp=sf_link")

zillow_search = ZillowRentalSearch()
zillow_search.get_listings()
zillow_search.fill_form(GOOGLE_FORM_URL)
