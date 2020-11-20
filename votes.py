import random
random.seed(0)

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]

def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

def results_hash (VOTES) : 
    candidates_results = {
        candidate : [0] * len(MENTIONS)
        for candidate in CANDIDATES.keys()
    }
    
    for vote in VOTES : 
        for candidate, mention in vote.items() : 
            candidates_results [candidate][mention] +=1
    return candidates_results

def majoritary_mentions_hash (candidates_results) : 
    r = {}     
    for candidate, candidates_results in candidates_results.items() : 
        cumulated_votes = 0
        for mention, vote_count in enumerate(candidates_results) : 
            cumulated_votes += vote_count
            if MEDIAN < cumulated_votes : 
                r[candidate] = {               
                    "mention" : mention,
                    "score" : cumulated_votes
                }               
                break
    return r

def sort_candidates_by (MENTIONS) : 
    unsorted = [(key, (mention ["mention"], mention ["score"])) for key, mention in MENTIONS.items()]
    swapped = True
    while swapped : 
        swapped = False
        for j in range (0, len(unsorted)-1) : 
            if unsorted [j+1] [1] > unsorted [j] [1] : 
                unsorted [j+1], unsorted[j] = unsorted[j], unsorted [j+1]
                swapped = True
    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1],
        }
        for candidate in unsorted
    ]

def print_results (results) :
    for i, result in enumerate (results) : 
        name = CANDIDATES[result["name"]]
        mention = MENTIONS[result["mention"]]
        score = result["score"] * 100. / VOTES 
        if i == 0 : 
            print("Gagnant : {} avec {:.2f}% de mentions {}".format(name, score, mention))
            continue
        else : 
            print("- {} avec {:.2f}% de mentions {}".format(name, score, mention))



def main():
    votes = create_votes()
    results = results_hash(votes)
    majoritary_mentions = majoritary_mentions_hash (results)
    sorted_candidates = sort_candidates_by(majoritary_mentions)
    print_results (sorted_candidates)

if __name__ == '__main__':
    main()