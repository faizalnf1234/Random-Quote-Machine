import '../styles/Quotebox.scss';
import React from 'react';
import Button from 'react-bootstrap/Button';
import $ from 'jquery';

export default class Quotebox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      quotesData:  [],
      currentQuote: [],
      currentAuthor: [],
      twitter: [],
    };
 }

  handleUpdateQuote = () => {
    this.getQuote()
  }

  getQuote = () => {
    var quotesData;
    $.ajax({
      headers: {
        Accept: 'application/json'
      },
      url:
        'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json',
      success: (res) => {
        quotesData = JSON.parse(res);
        var coba = Math.floor(Math.random() * quotesData.quotes.length)
        // console.log(quotesData.quotes[coba].quote);
        var currentQuote = quotesData.quotes[coba].quote;
        var currentAuthor = quotesData.quotes[coba].author;
        var twitter = 'https://twitter.com/intent/tweet?hashtags=quotes&related=freecodecamp&text="'+currentQuote+'"'+currentAuthor;
        this.setState({ currentQuote:currentQuote, currentAuthor:currentAuthor, twitter:twitter })
      }
    });
  }

  componentDidMount() {
    this.getQuote();
  }

  render() {
    return(
      <div>
        <div className="quotebox">
          <div className='row'>
            <div className="col">
              <center>
                <p className="quoteall">
                  <div className="quote">
                    <cite  id="text">"{this.state.currentQuote}"</cite>
                  </div>
                  <p className="author" id="author">--{this.state.currentAuthor}--</p>
                </p>
              </center>
            </div>
          </div>
          <div className='row'>
            <div className="col">
              <a href={ this.state.twitter }  className="btn btn-info twitter mr-4 mt-4"><span class="iconify mt-1" style={{color:"white"}} data-icon="mdi:twitter" data-width="30" data-height="30"></span></a>
            </div>
          </div>
        </div>
        <br/>
        <center>
          <Button id="new-quote" variant="info" onClick={() => { this.handleUpdateQuote(); }}>Other Quotes</Button>
        </center> 
      </div>
    );
  }
}
