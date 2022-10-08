#include <cstddef>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <iterator>
#include <vector>
std::vector<std::vector<uint8_t>> process_image(
        std::vector<uint8_t> const &image_data, // height * width grayscale
        size_t height, size_t width, size_t patch_size)
{
    std::vector<std::vector<uint8_t>> result;
    for (size_t i = 0; i < height; i += patch_size) {
        size_t h = std::min(patch_size, height - i);
        for (size_t j = 0; j < width; j += patch_size) {
            size_t w = std::min(patch_size, width - j);
            std::vector<uint8_t> patch(patch_size * patch_size, 0u);
            for (size_t r = 0, ri = i; r < h; ++r, ++ri)
                memcpy(&patch[r * patch_size], &image_data[ri * width + j], w);
            result.emplace_back(std::move(patch));
        }
    }
    return result;
}

// Вопрос: что возвращает функция process_image?
std::vector<uint8_t> revert(
        std::vector<std::vector<uint8_t>> const &patches,
        size_t height, size_t width, size_t patch_size)
{
    std::vector<uint8_t> result(height * width, 0u);
    size_t patch_per_row = width / patch_size + (width % patch_size != 0); // ceil

    for (size_t patch_i = 0; patch_i < patches.size(); patch_i++) {
    	std::vector<uint8_t> const &patch = patches[patch_i];

    	size_t col = patch_i % patch_per_row;
    	size_t row = patch_i / patch_per_row;

    	size_t copy_patch_size = patch_size;
    	size_t copy_patch_count = patch_size;
    	size_t cur_width = (col + 1) * patch_size;
    	size_t cur_height = (row + 1) * patch_size;
    	
    	if (cur_width > width) {
    		copy_patch_size = patch_size - (cur_width - width);
    	}
    	if (cur_height > height) {
    		copy_patch_count = patch_size - (cur_height - height);
    	}
        for (size_t ps = 0; ps < copy_patch_count; ++ps) {
        	memcpy(&result[row*width*patch_size+col*patch_size+ps*width], &patch[ps*patch_size], copy_patch_size);
        }
    }
    return result;
}

int main()
{
    std::vector<uint8_t> image_data = {
        10u, 11u, 12u,
        13u, 14u, 15u,
        16u, 17u, 18u,
        19u, 20u, 21u,
        22u, 23u, 24u,
    };
    std::vector<std::vector<uint8_t>> result = process_image(image_data, 5, 3, 2);
    for (std::vector<uint8_t> const &patch : result) {
        std::copy(patch.begin(), patch.end(),
                std::ostream_iterator<unsigned>(std::cout, ", "));
        std::cout << std::endl;
    }
    std::vector<uint8_t> image_data_2 = revert(result, 5, 3, 2);
    
    std::copy(image_data_2.begin(), image_data_2.end(),
                std::ostream_iterator<unsigned>(std::cout, ", "));
    std::cout << std::endl;
    return 0;
}