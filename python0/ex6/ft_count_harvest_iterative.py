# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_iterative.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:50:30 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:34:38 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative() -> None:
    day = int(input("Days until harvest: "))
    for i in range(1, day + 1):
        print(f"Day: {i}")
    print("Harvest time!")
