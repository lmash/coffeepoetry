from coffee import utils


def test_content_of_haiku_reduced_to_first_three_lines():
    content = "Golden beans dancing,\nLatte art blooming with love,\nTaste of darkness, bliss.\n\n" \
              "Friendly souls unite,\nIn this haven of aroma,\nBest coffee, by far."
    assert utils.reduce_content(content) == "Golden beans dancing,\n" \
                                            "Latte art blooming with love,\n" \
                                            "Taste of darkness, bliss."
