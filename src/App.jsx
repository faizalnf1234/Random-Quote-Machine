import React, { Component } from 'react';
import Header from './components/Header';
// import Quotebox from './components/Quotebox';
import QuoteAll from './components/QuoteAll';
 
class App extends Component {
  render() {
    return (
      <div className="content">
        <Header />
        <QuoteAll/>
        {/* <Quotebox /> */}
      </div>
    );
  }
}
 
export default App;