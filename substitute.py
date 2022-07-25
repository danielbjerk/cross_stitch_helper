from recipe import Thread
import dmc_lookup

def find_substitutes(query_threads, recipe, inventory):
    # simple implementation: one-to-one substitution
    dmc = dmc_lookup()
    subs = {}
    for thread in query_threads:
        ids = dmc.n_closest_colors(3, thread.RGB)
        for id in ids:
            if Thread("dmc", id) in inventory:
                subs[thread] = id
            
    return subs
    