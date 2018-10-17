import React, { Component } from 'react';
import './App.css';
import ReactDataGrid from 'react-data-grid';

const columns = [{ key: 'time', name: 'Time' }, { key: 'number', name: 'Employees Required' }];
//const rows = [{ time: "8:00 AM", number: '3' }, {time: "9:00 AM", number: '4'}];
//const rowGetter = rowNumber => rows[rowNumber];

class Grid extends Component {
constructor (props) {
    super(props)
    this.state = {
     	rows: [],
     	rowGetter: rowNumber => [][rowNumber],
    };
  }
componentDidUpdate(prevProps) {
  if (this.props.data !== prevProps.data) {
    this.setState({
	rows: this.props.data,
	rowGetter: rowNumber => this.props.data[rowNumber]
    });
  }
}
  render() {
    return (
         <ReactDataGrid
         columns={columns}
         rowGetter={this.state.rowGetter}
         rowsCount={this.state.rows.length}
         minHeight={500} />
    )
  }
}

export default Grid;
