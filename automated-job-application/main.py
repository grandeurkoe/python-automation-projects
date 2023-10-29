from linkedin import LinkedIn

URL = "https://in.linkedin.com/"

linkedin = LinkedIn(URL)

linkedin.sign_in()
linkedin.search_job_query()
linkedin.save_job_posting()

