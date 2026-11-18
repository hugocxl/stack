from scenes.redraws.review_approved import review_document

DESCRIPTION = "A clock badge overlaps a review document with a separate column of annotations."


def draw(s):
    review_document(s, "clock")
