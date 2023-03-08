import React from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Products from "./admin/Products";
import Main from "./main/Main";

function App() {
    return (

        <div className="App">


            <BrowserRouter>
                <Routes>
                    <Route path='/'  element={<Main/>}/>
                    <Route path='/admin/products' element={<Products/>}/>

                </Routes>
            </BrowserRouter>


        </div>
    );
}

export default App;
