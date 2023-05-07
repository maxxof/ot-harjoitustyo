import os

dirname = os.path.dirname(__file__)

class StorageController:
    """Luokka, joka on vastuussa pisteiden pysyväistallennuksesta
    
    Attributes:
        path: tallennustiedoston polku
    """

    def __init__(self):
        self.path = os.path.join(dirname, "storage/highscores.csv")

    def get_scores(self):
        with open(self.path, encoding="utf-8") as file:
            scores = []
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                username, score = line.split(";")
                scores.append((username, int(score)))
            return self.sort_by_score(scores)

    def save_score(self, username, score):
        scores = self.get_scores()

        scores.append((username, score))
        scores = self.sort_by_score(scores)[:5]

        with open(self.path, "w", encoding="utf-8" ) as file:
            for element in scores:
                line = f"{element[0]};{element[1]}\n"
                file.write(line)

    def sort_by_score(self, scores):
        return sorted(scores, key=lambda x: x[1], reverse=True)
