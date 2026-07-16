# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 18:26:30 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:33:30 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    total = harvest1+harvest2+harvest3
    print(f"Total harvest: {total}")
