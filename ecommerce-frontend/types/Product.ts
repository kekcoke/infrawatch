// src/types/Product.ts

export interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
    category: string;
    inStock: boolean;
    createdAt: string;
    updatedAt: string;
}

export interface ProductFormData {
    name: string;
    price: number;
    description: string;
    category: string;
    inStock: boolean;
}
