import React from 'react'


class NewManufacturer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name: '',
    }
    this.handleNameChange = this.handleNameChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleNameChange(event) {
    const value = event.target.value
    this.setState({name:value})
  }

  async handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state}

    const manufacturerUrl = 'http://localhost:8100/api/manufacturers/'
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const response = await fetch(manufacturerUrl, fetchConfig);
    if (response.ok) {

      const cleared = {
        name: '',
      }
      this.setState(cleared)
    }
  }


  render () {
    return (
      <div className="row">
        <div className="offset-3 col-6">

            <h1>Create a new manufacturer</h1>
            <form onSubmit={this.handleSubmit} id="create-manufacturer-form">
              <div className="form-floating mb-3">
                <input onChange={this.handleNameChange} placeholder="Name" required type="text" name="name" id="name" className="form-control" value={this.state.name} />
                <label htmlFor="name">Name</label>
              </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>

    )
  }

}

export default NewManufacturer
