#include <iostream>

void concat(int *num_list, int size)
{
	int	*max_list = new int[size];
	int	max;

	max_list[0] = num_list[0];
	max = num_list[0];
	for (int i = 1; i < size; i++)
	{
		max_list[i] = std::max(0, max_list[i - 1]) + num_list[i];
		if (max < max_list[i])
			max = max_list[i];
	}
	std::cout << max;
	return ;
}

int main(void)
{
	int size;
	int *num_list;

	scanf("%d", &size);
	num_list = new int[size];
	for (int i = 0; i < size; i++)
		scanf("%d", num_list + i);
	
	concat(num_list, size);
	return (0);
}