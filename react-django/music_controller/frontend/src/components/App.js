import React, { Component } from "react";
import { render } from "react-dom";

// component for react to inject into the HTML
export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (<h1> Testing React Code </h1>)
    }
}


// get the app container we want to inject into
const appDiv = document.getElementById(("app"));
// render passes the app component to the app div we want to modify
render(<App />, appDiv);