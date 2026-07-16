# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/20 13:31:54 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:32:41 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
