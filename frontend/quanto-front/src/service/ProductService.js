export const ProductService = {
    getProductsData() {
        return [
            {
                id: '1000',
                hours_in_projects: 'Bamboo Watch',
                hours_this_project: 'Product Description',
                pos: 65,
            },
            {
                id: '1001',
                hours_in_projects: 'Bamboo Watch',
                hours_this_project: 'Product Description',
                pos: 65,
            },
            {
                id: '1002',
                hours_in_projects: 'Bamboo Watch',
                hours_this_project: 'Product Description',
                pos: 65,
            },
        ];
    },

    getProductsMini() {
        return Promise.resolve(this.getProductsData().slice(0, 5));
    },

    getProductsSmall() {
        return Promise.resolve(this.getProductsData().slice(0, 10));
    },

    getProducts() {
        return Promise.resolve(this.getProductsData());
    },

    getProductsWithOrdersSmall() {
        return Promise.resolve(this.getProductsWithOrdersData().slice(0, 10));
    },

    getProductsWithOrders() {
        return Promise.resolve(this.getProductsWithOrdersData());
    }
};

