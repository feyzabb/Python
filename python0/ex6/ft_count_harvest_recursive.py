# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 21:28:35 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:37:42 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive(day: int | None = None,
                               cur_day: int = 1) -> None:
    if day is None:
        day = int(input("Days until harvest: "))
    if cur_day <= day:
        print(f"Day {cur_day}")
        ft_count_harvest_recursive(day, cur_day + 1)
    if cur_day == day:
        print("Harvest time!")
