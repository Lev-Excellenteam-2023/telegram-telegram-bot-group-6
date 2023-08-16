class Config:

    MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 100
    TEMPLATE_PREFIX_TO_OPENAI = "This is the estimate problem - {}," \
                                "ask me questions to make sure that the distinction is indeed correct "
