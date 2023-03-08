import React from 'react';
import './App.css';
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import {BrowserRouter, Route} from "react-router-dom";
import Products from "./admin/Products";

function App() {
    return (

        <div className="App">
            <Nav/>


            <div className="container-fluid">
                <div className="row">
                    <Menu/>

                    <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                        <BrowserRouter>
                            {/*<Route path='/admin/products' component={Products}/>*/}
                            <Route path='/admin/products'>
                                <Products/>
                            </Route>
                        </BrowserRouter>


                    </main>
                </div>
            </div>

        </div>
    );
}

export default App;
