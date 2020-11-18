def transform(data):
    """
    This function body should contain all the desired transformations on incoming DataFrame. Permitted builtin functions
    as well as permitted NumPy and Pandas objects and functions are available inside this function.
    Permitted NumPy and Pandas objects and functions can be used with aliases 'np' and 'pd' respectively.
    This function executes in a sandbox mode. Please refer the documentation for permitted objects and functions. Using
    any restricted functions or objects would cause an internal exception and result in a pipeline failure.
    Any code outside this function body will not be executed and inclusion of such code is discouraged.
    :param data: Pandas DataFrame
    :return: Pandas DataFrame
    """
    #####################################################
    # Provide the function body for data transformation #
    #####################################################

    words = [
        {
            "key": "good",
            "rating": 1
        },
        {
            "key": "best",
            "rating": 1
        },
        {
            "key": "great",
            "rating": 1
        },
        {
            "key": "excellent",
            "rating": 1
        },
        {
            "key": "happy",
            "rating": 1
        },
        {
            "key": "super",
            "rating": 1
        },
        {
            "key": "bad",
            "rating": -1
        },
        {
            "key": "fake",
            "rating": -1
        },
        {
            "key": "waste",
            "rating": -1
        },
        {
            "key": "expensive",
            "rating": -1
        },
        {
            "key": "broke",
            "rating": -1
        },
        {
            "key": "not",
            "rating": -1
        }
    ]

    def calculateSentiment(row):
        for word in words:
            if str(row['REVIEW_TITLE']).lower().find(word['key']) > -1:
                return word['rating']
  
        return 0

    data['SENTIMENT'] = data.apply(lambda row: calculateSentiment(row), 1, result_type='reduce')

    return data