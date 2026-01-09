import { Product, ProductFormData } from '../types/Product';
import { api } from './api';

export const productService = {
    getAllProducts: async (): Promise<Product[]> => {
        const response = await api.get<Product[]>('/api/products');
        return response.data;
    },

    getProduct: async (id: number): Promise<Product> => {
        const response = await api.get<Product>(`/api/products/${id}`);
        return response.data;
    },

    createProduct: async (productData: ProductFormData): Promise<Product> => {
        const response = await api.post<Product>('/api/products', productData);
        return response.data;
    },

    updateProduct: async (id: number, productData: ProductFormData): Promise<Product> => {
        const response = await api.put<Product>(`/api/products/${id}`, productData);
        return response.data;
    },

    deleteProduct: async (id: number): Promise<void> => {
        await api.delete(`/api/products/${id}`);
    },
}