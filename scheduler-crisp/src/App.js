import React, { Component } from 'react';
import './App.css';
import DatePicker from 'react-datepicker';
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';
import axios from 'axios';
import Grid from './Grid.js'; 

class App extends Component {
constructor (props) {
    super(props)
    this.state = {
      startDate: moment(),
      display: moment().format('LL'),
      data: [],
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(date) {
    this.setState({
      startDate: date,
      display: date.format('LL')
    });
     axios.get(`http://18.224.72.19:5000/?date=${date.format('LL')}`)
    .then(response => this.setState({ data: response.data }))
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>
	    Crisp Scheduler
          </h1>
	  <p>Please select a date to see worker needs for that day</p>
	  <DatePicker
            selected={this.state.startDate}
            onChange={this.handleChange}
           />
        </header>
	<h2>Schedule for {this.state.display} : </h2>
	<Grid data={this.state.data} />
      </div>
    );
  }
}

export default App;
