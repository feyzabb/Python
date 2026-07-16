# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_name.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 17:05:17 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:33:22 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_garden_name() -> None:
    garden_name = input("Enter garden name: ")
    print(f"Garden: {garden_name}")
    print("Status: Growing well!")


if __name__ == "__main__":
    ft_garden_name()
