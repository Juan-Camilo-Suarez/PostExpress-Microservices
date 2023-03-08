import React, {SyntheticEvent, useState} from 'react';
import Wrapper from "../Wrapper";
import {Simulate} from "react-dom/test-utils";
import { Navigate } from 'react-router-dom';

const ProductsCreate = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch('http://localhost:8000/api/products', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                description,
                image
            })
        });
        console.log(title, description ,image);

        setRedirect(true);
    }
    if (redirect) {
        return <Navigate to={'/admin/products'}/>
    }

    return (
        <div>
            <Wrapper>
                <form onSubmit={submit}>
                    <div className="form-group">
                        <label>Title</label>
                        <input type="text" className="form-control" name="title"
                               onChange={e => setTitle(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Description</label>
                        <input type="text" className="form-control" name="description"
                               onChange={e => setDescription(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label>Image</label>
                        <input type="text" className="form-control" name="image"
                               onChange={e => setImage(e.target.value)}
                        />
                    </div>
                    <button className="btn btn-outline-secondary">Save</button>
                </form>
            </Wrapper>

        </div>
    );
};

export default ProductsCreate;