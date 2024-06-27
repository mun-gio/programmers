def solution(nums):
    pokemons = {}
    for i in nums:
        if i not in pokemons:
            pokemons[i] = 1
        else:
            pokemons[i] += 1
    
    return len(nums)/2 if len(nums)/2 < len(pokemons) else len(pokemons)
