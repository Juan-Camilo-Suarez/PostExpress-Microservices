import React, {useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Link} from "react-router-dom";
import {Product} from "./interfaces/product";

const Products = () => {

    const [products, setProducts] = useState([]);


    // to get products from api
    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8000/api/products');

                const data = await response.json();

                console.log(data);
                setProducts(data);
            }
        )()
    }, [])
    return (
        <Wrapper>
            <div>
                <div className="table-responsive">
                    <table className="table table-striped table-sm">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Image</th>
                            <th>Title</th>
                            <th>Description</th>
                            <th>Likes</th>
                            <th>Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        {products.map((p: Product) => {
                            return (
                                <tr key={p.id}>
                                    <td>{p.id}</td>
                                    <td><img src={p.image} height="180"/></td>
                                    <td>{p.title}</td>
                                    <td>{p.description}</td>
                                    <td>{p.likes}</td>
                                    {/*<td>*/}
                                    {/*    <div className="btn-group mr-2">*/}
                                    {/*        <Link to={`/admin/products/${p.id}/edit`}*/}
                                    {/*              className="btn btn-sm btn-outline-secondary">Edit</Link>*/}
                                    {/*        <a href="#" className="btn btn-sm btn-outline-secondary"*/}
                                    {/*           onClick={() => del(p.id)}*/}
                                    {/*        >Delete</a>*/}
                                    {/*    </div>*/}
                                    {/*</td>*/}
                                </tr>
                            )
                        })}

                        </tbody>
                    </table>
                </div>

            </div>
        </Wrapper>

    );
};

export default Products;

